# 0413 workshop

> Goal
>
> - accounts CR
> - signup

### views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()
def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

### 결과 사진

![구현사진3](https://user-images.githubusercontent.com/60081201/79102920-ad137c80-7da6-11ea-90d8-505b02f3a1db.JPG)

![구현사진2](https://user-images.githubusercontent.com/60081201/79102926-aedd4000-7da6-11ea-850f-2e5e1abf123c.JPG)

![구현사진1](https://user-images.githubusercontent.com/60081201/79102927-aedd4000-7da6-11ea-8e3a-7547c49b40f9.JPG)