
from helpers.messages.warnings import message__warning__user_invalid_permissions_demonstrator

demonstrator_roles = [
    'admin',
    'advisor',
    'demonstrator',
    'lecturer'
]


async def is_authorised_demonstrator(ctx, new_or_edit, edit_ctx=None):
    for role in ctx.author.roles:
        if str(role).lower() in demonstrator_roles:
            return True

    if new_or_edit == 'NEW':
        await ctx.send(
            embed=message__warning__user_invalid_permissions_demonstrator(),
            hidden=True
        )
    elif new_or_edit == 'EDIT':
        await edit_ctx.edit_origin(
            embed=message__warning__user_invalid_permissions_demonstrator(),
            components=[]
        )
    return False
