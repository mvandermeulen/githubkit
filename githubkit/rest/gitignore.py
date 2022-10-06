"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api description.
See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import exclude_unset

from .models import GitignoreTemplate

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class GitignoreClient:
    def __init__(self, github: "GitHubCore"):
        self._github = github

    def get_all_templates(
        self,
    ) -> "Response[List[str]]":
        url = "/gitignore/templates"

        return self._github.request(
            "GET",
            url,
            response_model=List[str],
        )

    async def async_get_all_templates(
        self,
    ) -> "Response[List[str]]":
        url = "/gitignore/templates"

        return await self._github.arequest(
            "GET",
            url,
            response_model=List[str],
        )

    def get_template(
        self,
        name: str,
    ) -> "Response[GitignoreTemplate]":
        url = f"/gitignore/templates/{name}"

        return self._github.request(
            "GET",
            url,
            response_model=GitignoreTemplate,
        )

    async def async_get_template(
        self,
        name: str,
    ) -> "Response[GitignoreTemplate]":
        url = f"/gitignore/templates/{name}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=GitignoreTemplate,
        )
