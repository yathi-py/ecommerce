class MongoDB:
    """
    Django database router for routing specific app models to a MongoDB database.

    Attributes:
        - route_app_labels (set): Set of app labels to be routed to the MongoDB database.

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

        Args:
            - model: The Django model being read.
            - **hints: Additional hints for routing.

        Returns:
            - str or None: The MongoDB database alias if applicable, None otherwise.
        """
        if model._meta.app_label in self.route_app_labels:
            return "mongodb"
        return None

    def db_for_write(self, model, **hints):
        """
        Returns the MongoDB database alias for write operations.

        Args:
            - model: The Django model being written.
            - **hints: Additional hints for routing.

        Returns:
            - str or None: The MongoDB database alias if applicable, None otherwise.
        """
        if model._meta.app_label in self.route_app_labels:
            return "mongodb"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Determines if relations are allowed between objects.

        Args:
            - obj1: The first object in the relation.
            - obj2: The second object in the relation.
            - **hints: Additional hints for routing.

        Returns:
            - bool or None: True if relations are allowed, None otherwise.
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

        Args:
            - db: The database alias.
            - app_label: The app label of the model.
            - model_name: The name of the model.
            - **hints: Additional hints for routing.

        Returns:
            - bool or None: True if migration is allowed, None otherwise.
        """
        if app_label in self.route_app_labels:
            return db == "mongodb"
        return None
