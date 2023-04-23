import graphene

class Character(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    status = graphene.String()
    species = graphene.String()
    type = graphene.String()
    gender = graphene.String()
    origin = graphene.Field(lambda: OriginType)
    location = graphene.Field(lambda: LocationType)
    image = graphene.String()
    episodes = graphene.List(lambda: EpisodeType)
    episode = graphene.List(lambda: graphene.String)
    url = graphene.String()
    created = graphene.String()
