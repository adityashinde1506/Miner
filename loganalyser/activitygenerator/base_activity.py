
class BaseActivity:
    """
        Base class for all activities.
    """

    def perform_activity(self):
        raise NotImplementedError

    def repeat_perform_activity(self, wait_time, iterations):
        raise NotImplementedError

    def stop_activity(self):
        raise NotImplementedError
