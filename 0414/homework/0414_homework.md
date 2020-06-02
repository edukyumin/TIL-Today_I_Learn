# 0414_homework

## 1번

```python
is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
is_active = models.BooleanField(
    _('active'),
    default=True,
    help_text=_(
        'Designates whether this user should be treated as active. '
        'Unselect this instead of deleting accounts.'
    ),
```

## 2번

```python
max_length=150, 150자
```

## 3번

```
(a): AuthenticationForm
(b): login
(c): form.get_user()
```

## 4번

```
is_authenticated
```

## 5번

```
login_required
```

## 6번

```
SHA
```

## 7번

```
view에서 정의한 logout 함수와 import한 logout함수의 이름이 같아서
동작하지 않는다. logout을 import할때 이름을 auth_logout같은 형태로 바꿔서 import한다
from django.contrib.auth import logout as auth_logout 으로 바꾼다
```

