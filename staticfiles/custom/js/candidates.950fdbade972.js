$(document).ready(function () {
    const candidatesContainer = $('#candidates-container')
    const addCandidateBtn = $('#add-candidate-btn')
    let candidateIndex = $('#id_vote_candidate-TOTAL_FORMS').val();

    $(addCandidateBtn).on('click', function () {
        const newCandidateInput = $(`
        <div class="mb-3 candidate-input">
            <label for="id_vote_candidate-${candidateIndex}-name" class="form-label">Candidate ${parseInt(candidateIndex) + 1}</label>
            <input type="text" name="vote_candidate-${candidateIndex}-name" class="form-control" id="id_vote_candidate-${candidateIndex}-name" required>
            <div class="form-text">Insert name and profession</div>
        </div>
    `)
        candidatesContainer.append(newCandidateInput)

        // Update the TOTAL_FORMS count
        $('#id_vote_candidate-TOTAL_FORMS').val(parseInt(candidateIndex) + 1);
        candidateIndex++
    })
})