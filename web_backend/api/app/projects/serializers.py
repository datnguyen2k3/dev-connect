from rest_framework import serializers
from app.projects.models import Project, ProjectComment, SkillTag
from api.app.users.serializers import ProfileSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTag
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(read_only=True, many=False)

    class Meta:
        model = ProjectComment
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(read_only=True, many=False)
    tags = TagSerializer(read_only=True, many=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
        
    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer_reviews = ReviewSerializer(reviews, many=True)
        return serializer_reviews.data