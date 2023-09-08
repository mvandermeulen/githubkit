"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

    python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from datetime import date
from typing import TYPE_CHECKING, Dict, List, Literal, Optional, overload

from pydantic import BaseModel, TypeAdapter

from githubkit.utils import UNSET, Missing, exclude_unset

from .models import Root, BasicError, ApiOverview

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class MetaClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: "GitHubCore"):
        self._github = github

    def root(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[Root]":
        url = "/"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Root,
        )

    async def async_root(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[Root]":
        url = "/"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Root,
        )

    def get(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[ApiOverview]":
        url = "/meta"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ApiOverview,
        )

    async def async_get(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[ApiOverview]":
        url = "/meta"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ApiOverview,
        )

    def get_octocat(
        self,
        s: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[str]":
        url = "/octocat"

        params = {
            "s": s,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=str,
        )

    async def async_get_octocat(
        self,
        s: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[str]":
        url = "/octocat"

        params = {
            "s": s,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=str,
        )

    def get_all_versions(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[date]]":
        url = "/versions"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[date],
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_all_versions(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[date]]":
        url = "/versions"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[date],
            error_models={
                "404": BasicError,
            },
        )

    def get_zen(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[str]":
        url = "/zen"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=str,
        )

    async def async_get_zen(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[str]":
        url = "/zen"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=str,
        )
