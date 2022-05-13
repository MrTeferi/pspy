"""
Photoshop ScriptListenerJS to Python
"""
import photoshop.api as ps
app = ps.Application()


def s(name):
    """convert string name into type id"""
    return app.StringIDToTypeID(f"{name}")


def c(name):
    """convert char name into type id"""
    return app.CharIDToTypeID(f"{name}")


def ps_display_dialogs():
    """Dictionary with dialog constants"""
    return {"all": 1, "error": 2, "no": 3}


def dialog(dialog_type="no"):
    """Photoshop dialog windows settings using "all": 1, "error": 2, "no": 3"""
    dialogs = ps_display_dialogs()
    return dialogs.get(dialog_type, lambda: None)


def fill_0():
    desc13 = ps.ActionDescriptor()
    desc14 = ps.ActionDescriptor()
    desc14.PutUnitDouble(s("horizontal"), s("pixelsUnit"),  2024.000000)
    desc14.PutUnitDouble(s("vertical"), s("pixelsUnit"),  1836.000000)
    desc13.PutObject(s("from"), s("paint"),  desc14)
    desc13.PutInteger(s("tolerance"),  32)
    desc13.PutBoolean(s("antiAlias"), True)
    desc13.PutEnumerated(s("using"), s("fillContents"), s("foregroundColor"))
    app.ExecuteAction(s("fill"), desc13, dialog())

fill_0()
