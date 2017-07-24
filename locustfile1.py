import locust
class MyTaskSet(locust.TaskSet):

    @locust.task
    def do_get(self):
        self.client.get('/v2/home-mints?user_id=3&page=1')
class MyLocust(locust.HttpLocust):
    task_set = MyTaskSet

    min_wait = 900
    max_wait = 1100

    host = 'http://52.8.8.232:7006'
