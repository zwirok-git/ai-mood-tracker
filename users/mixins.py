from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OwnerRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object():
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


class DemoRestrictedMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.email == "test@test.com":
            messages.error(
                request,
                "Demo account cannot perform this action."
            )
            return redirect("profile-detail", pk=request.user.pk)

        return super().dispatch(request, *args, **kwargs)
