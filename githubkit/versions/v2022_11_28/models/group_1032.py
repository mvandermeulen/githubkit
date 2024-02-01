"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import Annotated

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof0(GitHubModel):
    """ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof0"""

    labels: Missing[List[str]] = Field(
        min_length=1,
        default=UNSET,
        description='The names of the labels to set for the issue. The labels you set replace any existing labels. You can pass an empty array to remove all labels. Alternatively, you can pass a single label as a `string` or an `array` of labels directly, but GitHub recommends passing an object with the `labels` key. You can also add labels to the existing labels for an issue. For more information, see "[Add labels to an issue](https://docs.github.com/rest/issues/labels#add-labels-to-an-issue)."',
    )


model_rebuild(ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof0)

__all__ = ("ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof0",)