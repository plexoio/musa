# Implemented in the same row
# of the voting card on the frontend, update if votecard status is set to completed

from django.db.models import Count


class WinnerView(AdminRequiredMixin, View):
    """View for displaying the winner of a vote."""

    def get(self, request, slug, *args, **kwargs):
        card = get_object_or_404(VoteCard, slug=slug)

        # Count the votes for each candidate
        vote_counts = VoteRecord.objects.filter(vote_card=card).values(
            'elected_person__name').annotate(vote_count=Count('elected_person')).order_by('-vote_count')

        # The candidate with the most votes is the first item in the queryset
        winner = vote_counts.first()

        return render(request, "winner.html", {"winner": winner})

    def post(self, request, slug, *args, **kwargs):
        card = get_object_or_404(VoteCard, slug=slug)

        # Count the votes for each candidate
        vote_counts = VoteRecord.objects.filter(vote_card=card).values(
            'elected_person').annotate(vote_count=Count('elected_person')).order_by('-vote_count')

        # The candidate with the most votes is the first item in the queryset
        winner_id = vote_counts.first()['elected_person']

        # Set is_elected to True for the winner
        elected_person = ElectedPerson.objects.get(id=winner_id)
        elected_person.is_elected = True
        elected_person.save()

        return redirect('winner_view', slug=card.slug)
