operation_parameter_map = {
    '/values/workersToNotify/workersToNotify-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'workers'
            },
        ]
    },
    '/values/feedbackTemplate/feedbackTemplate-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'templateType'
            },
            {
                'name': 'worker'
            },
        ]
    },
    '/values/feedbackOnWorker/feedbackOnWorker-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/values/feedbackResponder/feedbackResponder-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'templateType'
            },
            {
                'name': 'worker'
            },
        ]
    },
    '/values/relatesTo/relatesTo-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'relatesToTag'
            },
        ]
    },
    '/feedbackBadges/{ID}-GET': {
        'parameters': [
            {
                'name': 'ID'
            },
        ]
    },
    '/feedbackBadges-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/giveRequestedFeedbackEvents-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/giveRequestedFeedbackEvents/{ID}-GET': {
        'parameters': [
            {
                'name': 'ID'
            },
        ]
    },
    '/giveRequestedFeedbackEvents/{ID}-PATCH': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'dueDate'
            },
            {
                'name': 'feedbackGivenDate'
            },
            {
                'name': 'feedbackCreationDate'
            },
            {
                'name': 'requestedBy'
            },
            {
                'name': 'aboutWorker'
            },
            {
                'name': 'expirationDate'
            },
            {
                'name': 'displayNameofResponder'
            },
            {
                'name': 'feedbackComments'
            },
            {
                'name': 'businessProcessParameters'
            },
            {
                'name': 'feedbackPrivate'
            },
            {
                'name': 'feedbackConfidential'
            },
            {
                'name': 'id'
            },
            {
                'name': 'descriptor'
            },
        ]
    },
    '/workers/{ID}/anytimeFeedbackEvents-POST': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'toWorker'
            },
            {
                'name': 'workersToNotify'
            },
            {
                'name': 'relatesTo'
            },
            {
                'name': 'businessProcessParameters'
            },
            {
                'name': 'feedbackAlsoAbout'
            },
            {
                'name': 'hiddenFromWorker'
            },
            {
                'name': 'hiddenFromManager'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'fromWorker'
            },
            {
                'name': 'badge'
            },
            {
                'name': 'relatedFeedbackEvents'
            },
            {
                'name': 'feedbackGivenDate'
            },
            {
                'name': 'showFeedbackProviderName'
            },
            {
                'name': 'href'
            },
            {
                'name': 'id'
            },
            {
                'name': 'descriptor'
            },
        ]
    },
    '/workers-GET': {
        'parameters': [
            {
                'name': 'includeTerminatedWorkers'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/workers/{ID}/anytimeFeedbackEvents/{subresourceID}-GET': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'subresourceID'
            },
        ]
    },
    '/workers/{ID}/anytimeFeedbackEvents-GET': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/workers/{ID}/goals-GET': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/workers/{ID}/requestedFeedbackOnWorkerEvents/{subresourceID}-GET': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'subresourceID'
            },
        ]
    },
    '/workers/{ID}/requestedFeedbackOnWorkerEvents-GET': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/workers/{ID}/requestedFeedbackOnSelfEvents-GET': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/workers/{ID}/requestedFeedbackOnSelfEvents/{subresourceID}-GET': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'subresourceID'
            },
        ]
    },
    '/workers/{ID}/goals/{subresourceID}-GET': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'subresourceID'
            },
        ]
    },
    '/workers/{ID}-GET': {
        'parameters': [
            {
                'name': 'ID'
            },
        ]
    },
    '/workers/{ID}/requestedFeedbackOnSelfEvents-POST': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'businessProcessParameters'
            },
            {
                'name': 'feedbackQuestions'
            },
            {
                'name': 'feedbackAbout'
            },
            {
                'name': 'feedbackTemplate'
            },
            {
                'name': 'expirationDate'
            },
            {
                'name': 'requestDate'
            },
            {
                'name': 'feedbackOverallStatus'
            },
            {
                'name': 'feedbackPrivate'
            },
            {
                'name': 'feedbackResponders'
            },
            {
                'name': 'showFeedbackProviderName'
            },
            {
                'name': 'descriptor'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/workers/{ID}/requestedFeedbackOnWorkerEvents-POST': {
        'parameters': [
            {
                'name': 'ID'
            },
            {
                'name': 'feedbackAbout'
            },
            {
                'name': 'feedbackConfidential'
            },
            {
                'name': 'feedbackOverallStatus'
            },
            {
                'name': 'showFeedbackProviderName'
            },
            {
                'name': 'requestDate'
            },
            {
                'name': 'expirationDate'
            },
            {
                'name': 'feedbackQuestions'
            },
            {
                'name': 'feedbackTemplate'
            },
            {
                'name': 'feedbackResponders'
            },
            {
                'name': 'businessProcessParameters'
            },
            {
                'name': 'descriptor'
            },
            {
                'name': 'id'
            },
        ]
    },
};