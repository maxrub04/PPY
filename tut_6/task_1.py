from functools import wraps

current_user={
    'name': 'Max',
    'role': ["deleter","editer"]
}

def requires_role(role_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if role_name not in current_user["role"]:
                raise PermissionError(f"User '{current_user['name']}' doesnt have '{role_name}' role.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@requires_role("deleter")
def delete_post(id):
    return {f"id: {id} has been deleted"}
@requires_role("editer")
def edit_post(id):
    return {f"id: {id} has been edited"}
@requires_role("viewer")
def view_post(id):
    return {f"id: {id} has been viewed"}



print(delete_post(42)) # ✅ Should work (user has "admin")
print(edit_post(7)) # ✅ Should work (user has "editor")
print(view_post(99)) # ❌ Should raise PermissionError (user lacks "viewer")