class MongoDB:
    """
    Django database router for routing specific app models to a MongoDB database.

    Note:
        This router is designed to route models from specific apps to a MongoDB database.
    """

    route_app_labels = {"products"}
    """
    Set of app labels to be routed to the MongoDB database.
    """

    def db_for_read(self, model, **hints):
        """
        Returns the MongoDB database alias for read operations.
        """
        if model._meta.app_label in self.route_app_labels:
            return "mongodb"
        return None

    def db_for_write(self, model, **hints):
        """
        Returns the MongoDB database alias for write operations.
        """
        if model._meta.app_label in self.route_app_labels:
            return "mongodb"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Determines if relations are allowed between objects.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Determines if a migration is allowed.
        """
        if app_label in self.route_app_labels:
            return db == "mongodb"
        return None
