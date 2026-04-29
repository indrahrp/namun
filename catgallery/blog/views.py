import json
import os
import anthropic
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_write(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        raw = request.POST.get('raw_transcript', '').strip()
        if title and content:
            post = Post.objects.create(title=title, content=content, raw_transcript=raw)
            return redirect('blog:detail', pk=post.pk)
    return render(request, 'blog/post_write.html')


@require_POST
def improve_text(request):
    api_key = os.environ.get('ANTHROPIC_API_KEY', '')
    if not api_key:
        return JsonResponse({'error': 'ANTHROPIC_API_KEY not set. Add it to your .env file.'}, status=500)

    try:
        data = json.loads(request.body)
        raw_text = data.get('text', '').strip()
        if not raw_text:
            return JsonResponse({'error': 'No text provided.'}, status=400)

        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model='claude-sonnet-4-6',
            max_tokens=1024,
            messages=[{
                'role': 'user',
                'content': (
                    'You are a friendly writing assistant. The following text was spoken aloud and '
                    'transcribed by voice recognition — it may have filler words, run-on sentences, '
                    'or unclear phrasing. Rewrite it into clear, natural, well-structured sentences '
                    'while preserving the speaker\'s personal voice and meaning. '
                    'Fix grammar and word choice. Do not add extra information. '
                    'Return ONLY the improved text, nothing else.\n\n'
                    f'Transcript:\n{raw_text}'
                )
            }]
        )
        improved = message.content[0].text
        return JsonResponse({'improved': improved})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
