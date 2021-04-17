from allauth.account.adapter import DefaultAccountAdapter

class NoNewUserAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return False

