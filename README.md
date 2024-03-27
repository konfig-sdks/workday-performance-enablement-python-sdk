<div align="left">

[![Visit Workday](./header.png)](https://workday.com)

# Workday<a id="workday"></a>

The Performance Management service enables applications to access and create feedback about workers in the system.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`workdayperformanceenablement.prompt_values.get_instances`](#workdayperformanceenablementprompt_valuesget_instances)
  * [`workdayperformanceenablement.prompt_values.get_instances_0`](#workdayperformanceenablementprompt_valuesget_instances_0)
  * [`workdayperformanceenablement.prompt_values.get_instances_1`](#workdayperformanceenablementprompt_valuesget_instances_1)
  * [`workdayperformanceenablement.prompt_values.get_instances_2`](#workdayperformanceenablementprompt_valuesget_instances_2)
  * [`workdayperformanceenablement.prompt_values.get_instances_3`](#workdayperformanceenablementprompt_valuesget_instances_3)
  * [`workdayperformanceenablement.feedback_badges.get_by_id`](#workdayperformanceenablementfeedback_badgesget_by_id)
  * [`workdayperformanceenablement.feedback_badges.get_collection`](#workdayperformanceenablementfeedback_badgesget_collection)
  * [`workdayperformanceenablement.give_requested_feedback_events.get_collection_feedback_events`](#workdayperformanceenablementgive_requested_feedback_eventsget_collection_feedback_events)
  * [`workdayperformanceenablement.give_requested_feedback_events.get_instance`](#workdayperformanceenablementgive_requested_feedback_eventsget_instance)
  * [`workdayperformanceenablement.give_requested_feedback_events.update_event`](#workdayperformanceenablementgive_requested_feedback_eventsupdate_event)
  * [`workdayperformanceenablement.workers.create_feedback_event`](#workdayperformanceenablementworkerscreate_feedback_event)
  * [`workdayperformanceenablement.workers.get_collection_staffing`](#workdayperformanceenablementworkersget_collection_staffing)
  * [`workdayperformanceenablement.workers.get_feedback_event`](#workdayperformanceenablementworkersget_feedback_event)
  * [`workdayperformanceenablement.workers.get_feedback_events`](#workdayperformanceenablementworkersget_feedback_events)
  * [`workdayperformanceenablement.workers.get_goals`](#workdayperformanceenablementworkersget_goals)
  * [`workdayperformanceenablement.workers.get_requested_event`](#workdayperformanceenablementworkersget_requested_event)
  * [`workdayperformanceenablement.workers.get_requested_feedback_events`](#workdayperformanceenablementworkersget_requested_feedback_events)
  * [`workdayperformanceenablement.workers.get_self_requested_feedback`](#workdayperformanceenablementworkersget_self_requested_feedback)
  * [`workdayperformanceenablement.workers.get_self_requested_feedback_event`](#workdayperformanceenablementworkersget_self_requested_feedback_event)
  * [`workdayperformanceenablement.workers.get_single_goal`](#workdayperformanceenablementworkersget_single_goal)
  * [`workdayperformanceenablement.workers.get_staffing_information`](#workdayperformanceenablementworkersget_staffing_information)
  * [`workdayperformanceenablement.workers.request_feedback_on_self_events`](#workdayperformanceenablementworkersrequest_feedback_on_self_events)
  * [`workdayperformanceenablement.workers.request_feedback_on_worker_events`](#workdayperformanceenablementworkersrequest_feedback_on_worker_events)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Workday&serviceName=PerformanceEnablement&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from workday_performance_enablement_python_sdk import WorkdayPerformanceEnablement, ApiException

workdayperformanceenablement = WorkdayPerformanceEnablement(
)

try:
    get_instances_response = workdayperformanceenablement.prompt_values.get_instances(
        limit=1,
        offset=1,
        workers=[
        "string_example"
    ],
    )
    print(get_instances_response)
except ApiException as e:
    print("Exception when calling PromptValuesApi.get_instances: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from workday_performance_enablement_python_sdk import WorkdayPerformanceEnablement, ApiException

workdayperformanceenablement = WorkdayPerformanceEnablement(
)

async def main():
    try:
        get_instances_response = await workdayperformanceenablement.prompt_values.aget_instances(
            limit=1,
            offset=1,
            workers=[
        "string_example"
    ],
        )
        print(get_instances_response)
    except ApiException as e:
        print("Exception when calling PromptValuesApi.get_instances: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from workday_performance_enablement_python_sdk import WorkdayPerformanceEnablement, ApiException

workdayperformanceenablement = WorkdayPerformanceEnablement(
)

try:
    get_instances_response = workdayperformanceenablement.prompt_values.raw.get_instances(
        limit=1,
        offset=1,
        workers=[
        "string_example"
    ],
    )
    pprint(get_instances_response.body)
    pprint(get_instances_response.body["total"])
    pprint(get_instances_response.body["data"])
    pprint(get_instances_response.headers)
    pprint(get_instances_response.status)
    pprint(get_instances_response.round_trip_time)
except ApiException as e:
    print("Exception when calling PromptValuesApi.get_instances: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `workdayperformanceenablement.prompt_values.get_instances`<a id="workdayperformanceenablementprompt_valuesget_instances"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_response = workdayperformanceenablement.prompt_values.get_instances(
    limit=1,
    offset=1,
    workers=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### workers: List[`str`]<a id="workers-liststr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_performance_enablement_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/workersToNotify/workersToNotify` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.prompt_values.get_instances_0`<a id="workdayperformanceenablementprompt_valuesget_instances_0"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_0_response = workdayperformanceenablement.prompt_values.get_instances_0(
    limit=1,
    offset=1,
    template_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### template_type: `str`<a id="template_type-str"></a>

The feedback template type for this feedback event, either Feedback on Self, 133de7d11fea10001dbb45a701140098 or Feedback on Worker 133de7d11fea10001dbb45973dec0097. This field is required.

##### worker: `str`<a id="worker-str"></a>

The worker WID. This field is required for the Feedback on Worker template and not supported for the Feedback on Self template. It can't be the processing worker.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_performance_enablement_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/feedbackTemplate/feedbackTemplate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.prompt_values.get_instances_1`<a id="workdayperformanceenablementprompt_valuesget_instances_1"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_1_response = workdayperformanceenablement.prompt_values.get_instances_1(
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_performance_enablement_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/feedbackOnWorker/feedbackOnWorker` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.prompt_values.get_instances_2`<a id="workdayperformanceenablementprompt_valuesget_instances_2"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_2_response = workdayperformanceenablement.prompt_values.get_instances_2(
    limit=1,
    offset=1,
    template_type="string_example",
    worker="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### template_type: `str`<a id="template_type-str"></a>

The feedback template type for this feedback event, either Feedback on Self, 133de7d11fea10001dbb45a701140098 or Feedback on Worker 133de7d11fea10001dbb45973dec0097. This field is required.

##### worker: `str`<a id="worker-str"></a>

The worker WID. This field is required for the Feedback on Worker templateType and not supported for the Feedback on Self templateType. It can't be the processing worker.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_performance_enablement_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/feedbackResponder/feedbackResponder` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.prompt_values.get_instances_3`<a id="workdayperformanceenablementprompt_valuesget_instances_3"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_3_response = workdayperformanceenablement.prompt_values.get_instances_3(
    limit=1,
    offset=1,
    relates_to_tag="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### relates_to_tag: `str`<a id="relates_to_tag-str"></a>

The talent tag linked to the feedback question.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_performance_enablement_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/relatesTo/relatesTo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.feedback_badges.get_by_id`<a id="workdayperformanceenablementfeedback_badgesget_by_id"></a>

Retrieves a single Feedback Badge instance

Secured by: Give Feedback

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = workdayperformanceenablement.feedback_badges.get_by_id(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`FeedbackBadgeDetail9eab868ca81410001402525d054211f7`](./workday_performance_enablement_python_sdk/pydantic/feedback_badge_detail9eab868ca81410001402525d054211f7.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/feedbackBadges/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.feedback_badges.get_collection`<a id="workdayperformanceenablementfeedback_badgesget_collection"></a>

Retrieves all active Feedback Badges.

Secured by: Give Feedback

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_response = workdayperformanceenablement.feedback_badges.get_collection(
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`FeedbackBadgesGetCollectionResponse`](./workday_performance_enablement_python_sdk/pydantic/feedback_badges_get_collection_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/feedbackBadges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.give_requested_feedback_events.get_collection_feedback_events`<a id="workdayperformanceenablementgive_requested_feedback_eventsget_collection_feedback_events"></a>

Retrieves all requested feedback given events for the user that responded to the feedback request.

Secured by: Self-Service: Role Requested Feedback, Self-Service: Self Requested Feedback

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_feedback_events_response = workdayperformanceenablement.give_requested_feedback_events.get_collection_feedback_events(
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`GiveRequestedFeedbackEventsGetCollectionFeedbackEventsResponse`](./workday_performance_enablement_python_sdk/pydantic/give_requested_feedback_events_get_collection_feedback_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/giveRequestedFeedbackEvents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.give_requested_feedback_events.get_instance`<a id="workdayperformanceenablementgive_requested_feedback_eventsget_instance"></a>

Retrieves a single requested feedback given event instance for the user that responded to the feedback request.

Secured by: Self-Service: Role Requested Feedback, Self-Service: Self Requested Feedback

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instance_response = workdayperformanceenablement.give_requested_feedback_events.get_instance(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`GiveRequestedFeedbackDetailsD396fd5bffec10000e3eba1a70440000`](./workday_performance_enablement_python_sdk/pydantic/give_requested_feedback_details_d396fd5bffec10000e3eba1a70440000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/giveRequestedFeedbackEvents/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.give_requested_feedback_events.update_event`<a id="workdayperformanceenablementgive_requested_feedback_eventsupdate_event"></a>

Updates the Give Requested Feedback Event that matches the WID in the url, and the current authenticated user is a responder for the event.
This endpoint is equivalent to the Give Requested Feedback task in Workday.

Secured by: Give Requested Feedback REST+TG

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_event_response = workdayperformanceenablement.give_requested_feedback_events.update_event(
    body={
        "due_date": "2024-03-23T07:00:00.000Z",
        "feedback_given_date": "2024-03-23T07:00:00.000Z",
        "feedback_creation_date": "2024-03-23T07:00:00.000Z",
        "expiration_date": "2024-03-23T07:00:00.000Z",
        "display_nameof_responder": True,
        "feedback_private": True,
        "feedback_confidential": True,
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    due_date="2024-03-23T07:00:00.000Z",
    feedback_given_date="2024-03-23T07:00:00.000Z",
    feedback_creation_date="2024-03-23T07:00:00.000Z",
    requested_by=None,
    about_worker=None,
    expiration_date="2024-03-23T07:00:00.000Z",
    display_nameof_responder=True,
    feedback_comments=[
        {
            "feedback_declined": True,
            "feedback_decline_reason": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "numeric_answer": 523672239,
            "date_answer": "2024-03-23T07:00:00.000Z",
            "response": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    business_process_parameters=None,
    feedback_private=True,
    feedback_confidential=True,
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### due_date: `date`<a id="due_date-date"></a>

The date the business process needs to be completed.

##### feedback_given_date: `date`<a id="feedback_given_date-date"></a>

The date the feedback was provided.

##### feedback_creation_date: `date`<a id="feedback_creation_date-date"></a>

The date the feedback event was created.

##### requested_by: `RequestedByD396fd5bffec1000100f44a5808f0006`<a id="requested_by-requestedbyd396fd5bffec1000100f44a5808f0006"></a>

##### about_worker: `AboutWorkerD396fd5bffec1000100f44a5808f0005`<a id="about_worker-aboutworkerd396fd5bffec1000100f44a5808f0005"></a>

##### expiration_date: `date`<a id="expiration_date-date"></a>

The date the feedback request expires.

##### display_nameof_responder: `bool`<a id="display_nameof_responder-bool"></a>

True if the feedback provider's name is not displayed.

##### feedback_comments: List[`RequestedFeedbackCommentsD396fd5bffec10001393477e77870000`]<a id="feedback_comments-listrequestedfeedbackcommentsd396fd5bffec10001393477e77870000"></a>

The feedback comments for this feedback event. To include feedback comments in reports or notifications intended for Employees, use Feedback Comments for Self-Service Reporting instead.

##### business_process_parameters: `BusinessProcessParametersD396fd5bffec1000100f440bde4c0001`<a id="business_process_parameters-businessprocessparametersd396fd5bffec1000100f440bde4c0001"></a>

##### feedback_private: `bool`<a id="feedback_private-bool"></a>

Yes if the feedback is private between the feedback provider and the worker.

##### feedback_confidential: `bool`<a id="feedback_confidential-bool"></a>

Yes if the feedback is confidential between the feedback provider and the manager. Employees, or who the feedback is about, don't see confidential feedback.

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GiveRequestedFeedbackDetailsD396fd5bffec10000e3eba1a70440000`](./workday_performance_enablement_python_sdk/type/give_requested_feedback_details_d396fd5bffec10000e3eba1a70440000.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GiveRequestedFeedbackDetailsD396fd5bffec10000e3eba1a70440000`](./workday_performance_enablement_python_sdk/pydantic/give_requested_feedback_details_d396fd5bffec10000e3eba1a70440000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/giveRequestedFeedbackEvents/{ID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.workers.create_feedback_event`<a id="workdayperformanceenablementworkerscreate_feedback_event"></a>

Creates a single instance of feedback for each of the specified workers with the provided data. The worker is specified by the Workday ID of the worker. You can use a returned id from GET /workers in the Staffing service /staffing.

If you want to see the status of conditionally hidden attributes for this request, call this method with the wd-metadata-api-version header. Set the header value to v1 (or the latest Workday Metadata API version). When you specify the wd-metadata-api-version header, this method returns the response metadata, instead of the actual data.

This endpoint is equivalent to the Give Feedback task in Workday. This endpoint initiates the Give Feedback business process or the Give Feedback to Multiple Recipients business process based on the request.

Secured by: Give Feedback

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_feedback_event_response = workdayperformanceenablement.workers.create_feedback_event(
    body={
        "hidden_from_worker": True,
        "hidden_from_manager": True,
        "comment": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "feedback_given_date": "2024-03-23T07:00:00.000Z",
        "show_feedback_provider_name": True,
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    to_worker=None,
    workers_to_notify=[
        {
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    relates_to=None,
    business_process_parameters=None,
    feedback_also_about=[
        {
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    hidden_from_worker=True,
    hidden_from_manager=True,
    comment="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    from_worker=None,
    badge=None,
    related_feedback_events=[
        {
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    feedback_given_date="2024-03-23T07:00:00.000Z",
    show_feedback_provider_name=True,
    href="string_example",
    id="string_example",
    descriptor="Lorem ipsum dolor sit ame",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### to_worker: `ToWorkerF4946919a39f10000f03207b1f230000`<a id="to_worker-toworkerf4946919a39f10000f03207b1f230000"></a>

##### workers_to_notify: List[`WorkersToNotify9e478586f65410001035b6c26a4c0000`]<a id="workers_to_notify-listworkerstonotify9e478586f65410001035b6c26a4c0000"></a>

The workers that were selected to be notified of the feedback given event.

##### relates_to: `RelatesTo9d12ad407f0f10001c3949add7d40000`<a id="relates_to-relatesto9d12ad407f0f10001c3949add7d40000"></a>

##### business_process_parameters: `BusinessProcessParametersAfd6ac52d6251000117d0a60ed8b0000`<a id="business_process_parameters-businessprocessparametersafd6ac52d6251000117d0a60ed8b0000"></a>

##### feedback_also_about: List[`GetWorkersFeedbackAlsoAbout3ab333661034100010b5635b2f7a0302`]<a id="feedback_also_about-listgetworkersfeedbackalsoabout3ab333661034100010b5635b2f7a0302"></a>

The other workers this feedback event is about.

##### hidden_from_worker: `bool`<a id="hidden_from_worker-bool"></a>

True if the feedback event is confidential between the feedback provider and the manager. Workers don't see confidential feedback.

##### hidden_from_manager: `bool`<a id="hidden_from_manager-bool"></a>

True if the feedback event is private between the feedback provider and the worker. Private feedback isn't shared with managers.

##### comment: `str`<a id="comment-str"></a>

The comment text for an anytime feedback event.

##### from_worker: `FromWorkerAfd6ac52d62510001357f891ccfd0001`<a id="from_worker-fromworkerafd6ac52d62510001357f891ccfd0001"></a>

##### badge: `BadgeAfd6ac52d62510001357f891ccfd0003`<a id="badge-badgeafd6ac52d62510001357f891ccfd0003"></a>

##### related_feedback_events: List[`RelatedFeedbackEvents9708c966f04f10000e1e9b7f9a5c0000`]<a id="related_feedback_events-listrelatedfeedbackevents9708c966f04f10000e1e9b7f9a5c0000"></a>

The anytime feedback events for the multiple recipients event.

##### feedback_given_date: `date`<a id="feedback_given_date-date"></a>

The date the feedback was provided.

##### show_feedback_provider_name: `bool`<a id="show_feedback_provider_name-bool"></a>

True if the feedback provider's name has chosen to be displayed. Names not chosen to be displayed are not shared.

##### href: `str`<a id="href-str"></a>

A link to the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FeedbackEventDetailAfd6ac52d62510001086b5c85cd50000`](./workday_performance_enablement_python_sdk/type/feedback_event_detail_afd6ac52d62510001086b5c85cd50000.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FeedbackEventDetailAfd6ac52d62510001086b5c85cd50000`](./workday_performance_enablement_python_sdk/pydantic/feedback_event_detail_afd6ac52d62510001086b5c85cd50000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/anytimeFeedbackEvents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.workers.get_collection_staffing`<a id="workdayperformanceenablementworkersget_collection_staffing"></a>

Retrieves a collection of workers and current staffing information.

Secured by: Self-Service: Current Staffing Information, Worker Data: Public Worker Reports

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_staffing_response = workdayperformanceenablement.workers.get_collection_staffing(
    include_terminated_workers=True,
    limit=1,
    offset=1,
    search="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### include_terminated_workers: `bool`<a id="include_terminated_workers-bool"></a>

Include terminated workers in the output

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### search: `str`<a id="search-str"></a>

Searches workers by name or worker ID. The search is case-insensitive. You can include space-delimited search strings for an OR search.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkersGetCollectionStaffingResponse`](./workday_performance_enablement_python_sdk/pydantic/workers_get_collection_staffing_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.workers.get_feedback_event`<a id="workdayperformanceenablementworkersget_feedback_event"></a>

Retrieves a single feedback given event instance with the specified ID.

This endpoint is equivalent to the View Feedback task in Workday.

Secured by: Self-Service: Anytime Feedback, Worker Data: Anytime Feedback

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_feedback_event_response = workdayperformanceenablement.workers.get_feedback_event(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`FeedbackEventDetailAfd6ac52d62510001086b5c85cd50000`](./workday_performance_enablement_python_sdk/pydantic/feedback_event_detail_afd6ac52d62510001086b5c85cd50000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/anytimeFeedbackEvents/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.workers.get_feedback_events`<a id="workdayperformanceenablementworkersget_feedback_events"></a>

Retrieves all feedback given events about the specified worker. Could also return a feedback multiple recipient event.

This endpoint is equivalent to the View Feedback task in Workday.

Secured by: Self-Service: Anytime Feedback, Worker Data: Anytime Feedback

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_feedback_events_response = workdayperformanceenablement.workers.get_feedback_events(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkersGetFeedbackEventsResponse`](./workday_performance_enablement_python_sdk/pydantic/workers_get_feedback_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/anytimeFeedbackEvents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.workers.get_goals`<a id="workdayperformanceenablementworkersget_goals"></a>

Retrieves all goals for a worker with the specified ID. You can use a returned id from GET /workers in the Staffing service. The goal data includes name, description, category, tags, associated reviews, due date, completed date, status, creator, worker it is for, supporting organization goal, locked reason, and activity streamable item.

Secured by: Self-Service: Employee Goals, Worker Data: Employee Goals

Scope: Performance Enablement

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_goals_response = workdayperformanceenablement.workers.get_goals(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkersGetGoalsResponse`](./workday_performance_enablement_python_sdk/pydantic/workers_get_goals_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/goals` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.workers.get_requested_event`<a id="workdayperformanceenablementworkersget_requested_event"></a>

Retrieves a single requested feedback event instance for the specified worker. This endpoint is equivalent to the View Feedback and View Feedback by Request tasks in Workday.

Secured by: Self-Service: Role Requested Feedback, Worker Data: Role Requested Feedback

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_requested_event_response = workdayperformanceenablement.workers.get_requested_event(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`RequestedFeedbackOnWorkerEventDetail2b4c8a6ca069100035b8586e16c20000`](./workday_performance_enablement_python_sdk/pydantic/requested_feedback_on_worker_event_detail2b4c8a6ca069100035b8586e16c20000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/requestedFeedbackOnWorkerEvents/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.workers.get_requested_feedback_events`<a id="workdayperformanceenablementworkersget_requested_feedback_events"></a>

Retrieves all requested feedback events for the specified worker. This endpoint is equivalent to the View Feedback task in Workday.

Secured by: Self-Service: Role Requested Feedback, Worker Data: Role Requested Feedback

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_requested_feedback_events_response = workdayperformanceenablement.workers.get_requested_feedback_events(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkersGetRequestedFeedbackEventsResponse`](./workday_performance_enablement_python_sdk/pydantic/workers_get_requested_feedback_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/requestedFeedbackOnWorkerEvents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.workers.get_self_requested_feedback`<a id="workdayperformanceenablementworkersget_self_requested_feedback"></a>

Retrieves all self-requested feedback events for the specified worker. This endpoint is equivalent to the View Feedback task in Workday.

Secured by: Self-Service: Self Requested Feedback, Worker Data: Self Requested Feedback

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_self_requested_feedback_response = workdayperformanceenablement.workers.get_self_requested_feedback(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkersGetSelfRequestedFeedbackResponse`](./workday_performance_enablement_python_sdk/pydantic/workers_get_self_requested_feedback_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/requestedFeedbackOnSelfEvents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.workers.get_self_requested_feedback_event`<a id="workdayperformanceenablementworkersget_self_requested_feedback_event"></a>

Retrieves a single self-requested feedback event instance for the specified worker. This endpoint is equivalent to the View Feedback and View Feedback by Request tasks in Workday.

Secured by: Self-Service: Self Requested Feedback, Worker Data: Self Requested Feedback

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_self_requested_feedback_event_response = workdayperformanceenablement.workers.get_self_requested_feedback_event(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`RequestedFeedbackOnSelfEventDetail19acce0101b310002e6bf03e1bbc0000`](./workday_performance_enablement_python_sdk/pydantic/requested_feedback_on_self_event_detail19acce0101b310002e6bf03e1bbc0000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/requestedFeedbackOnSelfEvents/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.workers.get_single_goal`<a id="workdayperformanceenablementworkersget_single_goal"></a>

Retrieves a single goal instance for a worker with the specified ID. The goal data includes name, description, category, tags, associated reviews, due date, completed date, status, creator, worker it is for, supporting organization goal, locked reason, and activity streamable item.

Secured by: Self-Service: Employee Goals, Worker Data: Employee Goals

Scope: Performance Enablement

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_goal_response = workdayperformanceenablement.workers.get_single_goal(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsSummary2c793e888bcd100033e663075a2b0000`](./workday_performance_enablement_python_sdk/pydantic/goals_summary2c793e888bcd100033e663075a2b0000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/goals/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.workers.get_staffing_information`<a id="workdayperformanceenablementworkersget_staffing_information"></a>

Retrieves a collection of workers and current staffing information.

Secured by: Self-Service: Current Staffing Information, Worker Data: Public Worker Reports

Scope: Staffing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_staffing_information_response = workdayperformanceenablement.workers.get_staffing_information(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerDataC2466b0778c610000d1936006720000e`](./workday_performance_enablement_python_sdk/pydantic/worker_data_c2466b0778c610000d1936006720000e.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.workers.request_feedback_on_self_events`<a id="workdayperformanceenablementworkersrequest_feedback_on_self_events"></a>

Secured by: Get Feedback on Self REST+TG

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_feedback_on_self_events_response = workdayperformanceenablement.workers.request_feedback_on_self_events(
    body={
        "expiration_date": "2024-03-23T07:00:00.000Z",
        "request_date": "2024-03-23T07:00:00.000Z",
        "feedback_overall_status": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "feedback_private": True,
        "feedback_responders": [
            {
                "descriptor": "Lorem ipsum dolor sit ame",
            }
        ],
        "show_feedback_provider_name": True,
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    business_process_parameters=None,
    feedback_questions=[
        {
            "question": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    feedback_about=None,
    feedback_template=None,
    expiration_date="2024-03-23T07:00:00.000Z",
    request_date="2024-03-23T07:00:00.000Z",
    feedback_overall_status="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    feedback_private=True,
    feedback_responders=[
        {
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    show_feedback_provider_name=True,
    descriptor="Lorem ipsum dolor sit ame",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### business_process_parameters: `BusinessProcessParameters4db9c44d36231000134c7a5b6f3b0000`<a id="business_process_parameters-businessprocessparameters4db9c44d36231000134c7a5b6f3b0000"></a>

##### feedback_questions: List[`RequestedFeedbackQuestionFfdd5de32f7f1000144df0c21e640000`]<a id="feedback_questions-listrequestedfeedbackquestionffdd5de32f7f1000144df0c21e640000"></a>

Feedback questions used in requested feedback events.

##### feedback_about: `FeedbackAbout4db9c44d36231000134c7b8eb3800003`<a id="feedback_about-feedbackabout4db9c44d36231000134c7b8eb3800003"></a>

##### feedback_template: `FeedbackTemplate4db9c44d36231000134c7b8eb3800000`<a id="feedback_template-feedbacktemplate4db9c44d36231000134c7b8eb3800000"></a>

##### expiration_date: `date`<a id="expiration_date-date"></a>

The date the feedback request expires.

##### request_date: `date`<a id="request_date-date"></a>

The date the feedback request was initiated.

##### feedback_overall_status: `str`<a id="feedback_overall_status-str"></a>

Overall status of the requested feedback process.

##### feedback_private: `bool`<a id="feedback_private-bool"></a>

Private feedback between the feedback provider and the worker. Private feedback isn't shared with managers.

##### feedback_responders: List[`FeedbackRespondersFfdd5de32f7f100016dbb1b188d70000`]<a id="feedback_responders-listfeedbackrespondersffdd5de32f7f100016dbb1b188d70000"></a>

The respondents who've been requested to provide feedback.

##### show_feedback_provider_name: `bool`<a id="show_feedback_provider_name-bool"></a>

Whether to display the name of the responders or have them remain anonymous.

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RequestedFeedbackOnSelfEventDetail19acce0101b310002e6bf03e1bbc0000`](./workday_performance_enablement_python_sdk/type/requested_feedback_on_self_event_detail19acce0101b310002e6bf03e1bbc0000.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RequestedFeedbackOnSelfEventDetail19acce0101b310002e6bf03e1bbc0000`](./workday_performance_enablement_python_sdk/pydantic/requested_feedback_on_self_event_detail19acce0101b310002e6bf03e1bbc0000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/requestedFeedbackOnSelfEvents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperformanceenablement.workers.request_feedback_on_worker_events`<a id="workdayperformanceenablementworkersrequest_feedback_on_worker_events"></a>

Not applicable.

Secured by: Get Feedback on \~Worker\~ REST+TG

Scope: Performance Enablement, Worker Profile and Skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_feedback_on_worker_events_response = workdayperformanceenablement.workers.request_feedback_on_worker_events(
    body={
        "feedback_confidential": True,
        "feedback_overall_status": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "show_feedback_provider_name": True,
        "request_date": "2024-03-23T07:00:00.000Z",
        "expiration_date": "2024-03-23T07:00:00.000Z",
        "feedback_responders": [
            {
                "descriptor": "Lorem ipsum dolor sit ame",
            }
        ],
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    feedback_about=None,
    feedback_confidential=True,
    feedback_overall_status="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    show_feedback_provider_name=True,
    request_date="2024-03-23T07:00:00.000Z",
    expiration_date="2024-03-23T07:00:00.000Z",
    feedback_questions=[
        {
            "question": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    feedback_template=None,
    feedback_responders=[
        {
            "descriptor": "Lorem ipsum dolor sit ame",
        }
    ],
    business_process_parameters=None,
    descriptor="Lorem ipsum dolor sit ame",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### feedback_about: `FeedbackAbout2b4c8a6ca069100035b85907ae2c0002`<a id="feedback_about-feedbackabout2b4c8a6ca069100035b85907ae2c0002"></a>

##### feedback_confidential: `bool`<a id="feedback_confidential-bool"></a>

Yes if the feedback is confidential between the feedback provider and the manager. Workers don't see confidential feedback.

##### feedback_overall_status: `str`<a id="feedback_overall_status-str"></a>

Overall status of the requested feedback process.

##### show_feedback_provider_name: `bool`<a id="show_feedback_provider_name-bool"></a>

Whether to display the name of the responders or have them remain anonymous.ccc

##### request_date: `date`<a id="request_date-date"></a>

The date the feedback request was initiated.

##### expiration_date: `date`<a id="expiration_date-date"></a>

The date the feedback request expires.

##### feedback_questions: List[`RequestedFeedbackQuestionFfdd5de32f7f1000144df0c21e640000`]<a id="feedback_questions-listrequestedfeedbackquestionffdd5de32f7f1000144df0c21e640000"></a>

Feedback questions used in requested feedback events.

##### feedback_template: `FeedbackTemplate2b4c8a6ca069100035b859a141200001`<a id="feedback_template-feedbacktemplate2b4c8a6ca069100035b859a141200001"></a>

##### feedback_responders: List[`FeedbackRespondersFfdd5de32f7f100016dbb1b188d70000`]<a id="feedback_responders-listfeedbackrespondersffdd5de32f7f100016dbb1b188d70000"></a>

The respondents who've been requested to provide feedback.

##### business_process_parameters: `BusinessProcessParameters2b4c8a6ca069100035b85907ae2c0000`<a id="business_process_parameters-businessprocessparameters2b4c8a6ca069100035b85907ae2c0000"></a>

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RequestedFeedbackOnWorkerEventDetail2b4c8a6ca069100035b8586e16c20000`](./workday_performance_enablement_python_sdk/type/requested_feedback_on_worker_event_detail2b4c8a6ca069100035b8586e16c20000.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RequestedFeedbackOnWorkerEventDetail2b4c8a6ca069100035b8586e16c20000`](./workday_performance_enablement_python_sdk/pydantic/requested_feedback_on_worker_event_detail2b4c8a6ca069100035b8586e16c20000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{ID}/requestedFeedbackOnWorkerEvents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
