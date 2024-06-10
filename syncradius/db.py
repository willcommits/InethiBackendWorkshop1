class RDRouter(object):
    """A router to control db operations."""

    table = {"syncradius": "rd"}

    def db_for_read(self, model, **hints):
        """Read from RD if model is from RD, else default."""
        return self.table.get(model._meta.app_label)

    def db_for_write(self, model, **hints):
        """Write to RD if model is from RD, else default."""
        return self.table.get(model._meta.app_label)

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if obj1._meta.app_label in self.table or obj2._meta.app_label in self.table:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        default database.
        """
        return False
