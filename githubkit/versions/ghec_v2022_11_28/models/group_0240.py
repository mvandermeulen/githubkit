"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ContentSymlink(GitHubModel):
    """Symlink Content

    An object describing a symlink
    """

    type: Literal["symlink"] = Field()
    target: str = Field()
    size: int = Field()
    name: str = Field()
    path: str = Field()
    sha: str = Field()
    url: str = Field()
    git_url: Union[str, None] = Field()
    html_url: Union[str, None] = Field()
    download_url: Union[str, None] = Field()
    links: ContentSymlinkPropLinks = Field(alias="_links")


class ContentSymlinkPropLinks(GitHubModel):
    """ContentSymlinkPropLinks"""

    git: Union[str, None] = Field()
    html: Union[str, None] = Field()
    self_: str = Field(alias="self")


model_rebuild(ContentSymlink)
model_rebuild(ContentSymlinkPropLinks)

__all__ = (
    "ContentSymlink",
    "ContentSymlinkPropLinks",
)
