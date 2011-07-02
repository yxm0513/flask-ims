from flask import Module, render_template

mod = Module(__name__)

# URL

def _(string):
    return string

@mod.errorhandler(404)
def page_not_found(error):
    if request.is_xhr:
        return jsonify(error=_('Sorry, page not found'))
    return render_template("error/404.html", error=error)

@mod.errorhandler(403)
def forbidden(error):
    if request.is_xhr:
        return jsonify(error=_('Sorry, not allowed'))
    return render_template("error/403.html", error=error)

@mod.errorhandler(500)
def server_error(error):
    if request.is_xhr:
        return jsonify(error=_('Sorry, an error has occurred'))
    return render_template("error/500.html", error=error)

@mod.errorhandler(401)
def unauthorized(error):
    if request.is_xhr:
        return jsonfiy(error=_("Login required"))
    flash(_("Please login to see this page"), "error")
    return redirect(url_for("account.login", next=request.path))
