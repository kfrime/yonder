#!/usr/bin/env python3

from sim.exceptions import abort
from .. import app, db, cache_pool
from ..model import User, Category
from ..consts import RespCode, Permission, RoleUser, RoleAdmin, Roles, USER, CATEGORY, ARTICLE
from ..decorators import permission_required, login_required


@app.route('/api/category', methods=('POST', ))
@permission_required(Permission.admin)
def category_create(ctx):
    input_json = ctx.request.json()
    if not input_json or "name" not in input_json:
        abort(RespCode.error, "field `name` is required")

    name = Category.valid_name(input_json['name'])

    # check if category name existed
    if Category.find_by_name(name) is not None:
        abort(RespCode.error, f"name `{name}` existed")

    cate = Category()
    cate.name = name
    cate.status = CATEGORY.status.active

    cate.save()
    if getattr(cate, 'id', None) is None:
        abort(RespCode.error, "create new user error")

    return cate


@app.route('/api/category/:cid')
def category_retrieve(ctx):
    cid = ctx.request.get_param('cid')
    try:
        cid = int(cid)
    except Exception as e:
        app.logger.error(f"cid must be an integer, but get cid: {cid}")
        abort(RespCode.error, "in GET method, cid must be an integer")

    cate = Category.find(cid)
    if not cate:
        abort(RespCode.error, "category not found")

    return cate
