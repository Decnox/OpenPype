import pyblish.api


class CollectReview(pyblish.api.InstancePlugin):
    """Collect review instance from rendered frames
    """

    order = pyblish.api.CollectorOrder + 0.3
    family = "review"
    label = "Collect Review"
    hosts = ["nuke"]
    families = ["write"]

    family_targets = [".local", ".frames"]

    def process(self, instance):
        families = [(f, search) for f in instance.data["families"]
                    for search in self.family_targets
                    if search in f][0]

        if families:
            root_femilies = families[0].replace(families[1], "")
            instance.data["families"].append(".".join([
                root_femilies,
                self.family
            ]))
            self.log.info("Review collected: `{}`".format(instance))
