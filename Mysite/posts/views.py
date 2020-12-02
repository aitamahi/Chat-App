from django.shortcuts import render,redirect
from .models import Posts
# Create your views here.
def post_commeent_create_and_list_view(request):
	qs=Posts.objects.all()

	context={
		'qs':qs,

	}
	return render(request,'main2.html',context)

def like_unlike_post(request):
	user=request.user
	if request.method =='POST':
		post_id=request.post.get('post_id')
		post_obj=post.objects.get(id='post_id')
		profile=profile.objects.get(user=user)

		if profile in post_obj.liked.all():
			post_obj.like.remove(profile)
		else:
			post_obj.liked.add(profile)
		like,created=Like.objects.get_or_create(user=profile,post_id=post_id)

		if not created:
			if like.value=='Like':
				like.value='Unlike'
			else:
				like.value='Like'
			post_obj.save()
			like.save()
	return redirect('posts:like-post-view')