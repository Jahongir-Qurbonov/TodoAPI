def autoCreateSuperUser():
    from django.contrib.auth.models import User as user_model

    super_users = user_model.objects.filter(is_superuser=True)
    if not super_users:
        super_user = user_model.objects.create_superuser(
            username="superuser", password="superuser"
        )
        if super_user.id:
            print("===> Successful create default superuser")


def autoCreateDjangoSite(env):
    from django.contrib.sites.models import Site

    sites = Site.objects.all()
    example_site = Site.objects.filter(name="example.com")
    if not sites.exists() or (example_site.exists() and sites.count() == 1):
        new_site = Site.objects.create(domain="127.0.0.1:8000", name="127.0.0.1:8000")
        if new_site.id:
            print(f"===> Saccessful create site -> {new_site.name}")
            try:
                env.int("SITE_ID")
            except:
                with open("./.env", "a+") as envfile:
                    envfile.write(f"SITE_ID={new_site.id}\n")
                    print("===> Create SITE_ID variable in .env")
                env.read_env()


def auto_configure(env):
    # set_random_generate_secret_key(env) # this migrated to settings.py

    autoCreateSuperUser()
    autoCreateDjangoSite(env)


def run():
    from config.settings import env

    auto_configure(env)
