from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OwnerRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object():
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


class DemoRestrictedMixin:
    def post(self, request, *args, **kwargs):
        if request.user.email == "test@test.com":
            messages.error(
                request,
                "Test account cannot be modified."
            )

            return redirect("account:profile-detail", request.user.pk)

        return super().post(request, *args, **kwargs)
