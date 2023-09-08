"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

    python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, Dict, List, Literal, Optional, overload

from pydantic import BaseModel, TypeAdapter

from githubkit.utils import UNSET, Missing, exclude_unset

from .models import License, BasicError, LicenseSimple, LicenseContent

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class LicensesClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: "GitHubCore"):
        self._github = github

    def get_all_commonly_used(
        self,
        featured: Missing[bool] = UNSET,
        per_page: Missing[int] = 30,
        page: Missing[int] = 1,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[LicenseSimple]]":
        url = "/licenses"

        params = {
            "featured": featured,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[LicenseSimple],
        )

    async def async_get_all_commonly_used(
        self,
        featured: Missing[bool] = UNSET,
        per_page: Missing[int] = 30,
        page: Missing[int] = 1,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[LicenseSimple]]":
        url = "/licenses"

        params = {
            "featured": featured,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[LicenseSimple],
        )

    def get(
        self,
        license_: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[License]":
        url = f"/licenses/{license}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=License,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get(
        self,
        license_: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[License]":
        url = f"/licenses/{license}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=License,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    def get_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[LicenseContent]":
        url = f"/repos/{owner}/{repo}/license"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=LicenseContent,
        )

    async def async_get_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[LicenseContent]":
        url = f"/repos/{owner}/{repo}/license"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=LicenseContent,
        )
