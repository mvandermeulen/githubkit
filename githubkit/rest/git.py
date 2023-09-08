"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

    python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, Dict, List, Literal, Optional, overload

from pydantic import BaseModel, TypeAdapter

from githubkit.utils import UNSET, Missing, exclude_unset

from .models import (
    Blob,
    GitRef,
    GitTag,
    GitTree,
    GitCommit,
    ShortBlob,
    BasicError,
    ValidationError,
    ReposOwnerRepoGitRefsPostBody,
    ReposOwnerRepoGitTagsPostBody,
    ReposOwnerRepoGitBlobsPostBody,
    ReposOwnerRepoGitTreesPostBody,
    ReposOwnerRepoGitCommitsPostBody,
    ReposOwnerRepoGitRefsRefPatchBody,
)
from .types import (
    ReposOwnerRepoGitRefsPostBodyType,
    ReposOwnerRepoGitTagsPostBodyType,
    ReposOwnerRepoGitBlobsPostBodyType,
    ReposOwnerRepoGitTreesPostBodyType,
    ReposOwnerRepoGitCommitsPostBodyType,
    ReposOwnerRepoGitRefsRefPatchBodyType,
    ReposOwnerRepoGitTagsPostBodyPropTaggerType,
    ReposOwnerRepoGitCommitsPostBodyPropAuthorType,
    ReposOwnerRepoGitTreesPostBodyPropTreeItemsType,
    ReposOwnerRepoGitCommitsPostBodyPropCommitterType,
)

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class GitClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: "GitHubCore"):
        self._github = github

    @overload
    def create_blob(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitBlobsPostBodyType,
    ) -> "Response[ShortBlob]":
        ...

    @overload
    def create_blob(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        content: str,
        encoding: Missing[str] = "utf-8",
    ) -> "Response[ShortBlob]":
        ...

    def create_blob(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitBlobsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[ShortBlob]":
        url = f"/repos/{owner}/{repo}/git/blobs"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoGitBlobsPostBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ShortBlob,
            error_models={
                "404": BasicError,
                "409": BasicError,
                "403": BasicError,
                "422": ValidationError,
            },
        )

    @overload
    async def async_create_blob(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitBlobsPostBodyType,
    ) -> "Response[ShortBlob]":
        ...

    @overload
    async def async_create_blob(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        content: str,
        encoding: Missing[str] = "utf-8",
    ) -> "Response[ShortBlob]":
        ...

    async def async_create_blob(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitBlobsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[ShortBlob]":
        url = f"/repos/{owner}/{repo}/git/blobs"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoGitBlobsPostBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ShortBlob,
            error_models={
                "404": BasicError,
                "409": BasicError,
                "403": BasicError,
                "422": ValidationError,
            },
        )

    def get_blob(
        self,
        owner: str,
        repo: str,
        file_sha: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[Blob]":
        url = f"/repos/{owner}/{repo}/git/blobs/{file_sha}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Blob,
            error_models={
                "404": BasicError,
                "422": ValidationError,
                "403": BasicError,
            },
        )

    async def async_get_blob(
        self,
        owner: str,
        repo: str,
        file_sha: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[Blob]":
        url = f"/repos/{owner}/{repo}/git/blobs/{file_sha}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Blob,
            error_models={
                "404": BasicError,
                "422": ValidationError,
                "403": BasicError,
            },
        )

    @overload
    def create_commit(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitCommitsPostBodyType,
    ) -> "Response[GitCommit]":
        ...

    @overload
    def create_commit(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        message: str,
        tree: str,
        parents: Missing[List[str]] = UNSET,
        author: Missing[ReposOwnerRepoGitCommitsPostBodyPropAuthorType] = UNSET,
        committer: Missing[ReposOwnerRepoGitCommitsPostBodyPropCommitterType] = UNSET,
        signature: Missing[str] = UNSET,
    ) -> "Response[GitCommit]":
        ...

    def create_commit(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitCommitsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitCommit]":
        url = f"/repos/{owner}/{repo}/git/commits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoGitCommitsPostBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitCommit,
            error_models={
                "422": ValidationError,
                "404": BasicError,
            },
        )

    @overload
    async def async_create_commit(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitCommitsPostBodyType,
    ) -> "Response[GitCommit]":
        ...

    @overload
    async def async_create_commit(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        message: str,
        tree: str,
        parents: Missing[List[str]] = UNSET,
        author: Missing[ReposOwnerRepoGitCommitsPostBodyPropAuthorType] = UNSET,
        committer: Missing[ReposOwnerRepoGitCommitsPostBodyPropCommitterType] = UNSET,
        signature: Missing[str] = UNSET,
    ) -> "Response[GitCommit]":
        ...

    async def async_create_commit(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitCommitsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitCommit]":
        url = f"/repos/{owner}/{repo}/git/commits"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoGitCommitsPostBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitCommit,
            error_models={
                "422": ValidationError,
                "404": BasicError,
            },
        )

    def get_commit(
        self,
        owner: str,
        repo: str,
        commit_sha: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[GitCommit]":
        url = f"/repos/{owner}/{repo}/git/commits/{commit_sha}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitCommit,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_commit(
        self,
        owner: str,
        repo: str,
        commit_sha: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[GitCommit]":
        url = f"/repos/{owner}/{repo}/git/commits/{commit_sha}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitCommit,
            error_models={
                "404": BasicError,
            },
        )

    def list_matching_refs(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[GitRef]]":
        url = f"/repos/{owner}/{repo}/git/matching-refs/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[GitRef],
        )

    async def async_list_matching_refs(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[GitRef]]":
        url = f"/repos/{owner}/{repo}/git/matching-refs/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[GitRef],
        )

    def get_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[GitRef]":
        url = f"/repos/{owner}/{repo}/git/ref/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitRef,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[GitRef]":
        url = f"/repos/{owner}/{repo}/git/ref/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitRef,
            error_models={
                "404": BasicError,
            },
        )

    @overload
    def create_ref(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitRefsPostBodyType,
    ) -> "Response[GitRef]":
        ...

    @overload
    def create_ref(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        ref: str,
        sha: str,
    ) -> "Response[GitRef]":
        ...

    def create_ref(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitRefsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitRef]":
        url = f"/repos/{owner}/{repo}/git/refs"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoGitRefsPostBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitRef,
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    async def async_create_ref(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitRefsPostBodyType,
    ) -> "Response[GitRef]":
        ...

    @overload
    async def async_create_ref(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        ref: str,
        sha: str,
    ) -> "Response[GitRef]":
        ...

    async def async_create_ref(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitRefsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitRef]":
        url = f"/repos/{owner}/{repo}/git/refs"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoGitRefsPostBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitRef,
            error_models={
                "422": ValidationError,
            },
        )

    def delete_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/git/refs/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "DELETE",
            url,
            headers=exclude_unset(headers),
            error_models={
                "422": ValidationError,
            },
        )

    async def async_delete_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/git/refs/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "DELETE",
            url,
            headers=exclude_unset(headers),
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    def update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitRefsRefPatchBodyType,
    ) -> "Response[GitRef]":
        ...

    @overload
    def update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        sha: str,
        force: Missing[bool] = False,
    ) -> "Response[GitRef]":
        ...

    def update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitRefsRefPatchBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitRef]":
        url = f"/repos/{owner}/{repo}/git/refs/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoGitRefsRefPatchBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitRef,
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    async def async_update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitRefsRefPatchBodyType,
    ) -> "Response[GitRef]":
        ...

    @overload
    async def async_update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        sha: str,
        force: Missing[bool] = False,
    ) -> "Response[GitRef]":
        ...

    async def async_update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitRefsRefPatchBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitRef]":
        url = f"/repos/{owner}/{repo}/git/refs/{ref}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoGitRefsRefPatchBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitRef,
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    def create_tag(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitTagsPostBodyType,
    ) -> "Response[GitTag]":
        ...

    @overload
    def create_tag(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        tag: str,
        message: str,
        object_: str,
        type: Literal["commit", "tree", "blob"],
        tagger: Missing[ReposOwnerRepoGitTagsPostBodyPropTaggerType] = UNSET,
    ) -> "Response[GitTag]":
        ...

    def create_tag(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitTagsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitTag]":
        url = f"/repos/{owner}/{repo}/git/tags"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoGitTagsPostBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitTag,
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    async def async_create_tag(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitTagsPostBodyType,
    ) -> "Response[GitTag]":
        ...

    @overload
    async def async_create_tag(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        tag: str,
        message: str,
        object_: str,
        type: Literal["commit", "tree", "blob"],
        tagger: Missing[ReposOwnerRepoGitTagsPostBodyPropTaggerType] = UNSET,
    ) -> "Response[GitTag]":
        ...

    async def async_create_tag(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitTagsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitTag]":
        url = f"/repos/{owner}/{repo}/git/tags"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoGitTagsPostBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitTag,
            error_models={
                "422": ValidationError,
            },
        )

    def get_tag(
        self,
        owner: str,
        repo: str,
        tag_sha: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[GitTag]":
        url = f"/repos/{owner}/{repo}/git/tags/{tag_sha}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitTag,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_tag(
        self,
        owner: str,
        repo: str,
        tag_sha: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[GitTag]":
        url = f"/repos/{owner}/{repo}/git/tags/{tag_sha}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=GitTag,
            error_models={
                "404": BasicError,
            },
        )

    @overload
    def create_tree(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitTreesPostBodyType,
    ) -> "Response[GitTree]":
        ...

    @overload
    def create_tree(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        tree: List[ReposOwnerRepoGitTreesPostBodyPropTreeItemsType],
        base_tree: Missing[str] = UNSET,
    ) -> "Response[GitTree]":
        ...

    def create_tree(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitTreesPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitTree]":
        url = f"/repos/{owner}/{repo}/git/trees"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoGitTreesPostBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitTree,
            error_models={
                "422": ValidationError,
                "404": BasicError,
                "403": BasicError,
            },
        )

    @overload
    async def async_create_tree(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoGitTreesPostBodyType,
    ) -> "Response[GitTree]":
        ...

    @overload
    async def async_create_tree(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        tree: List[ReposOwnerRepoGitTreesPostBodyPropTreeItemsType],
        base_tree: Missing[str] = UNSET,
    ) -> "Response[GitTree]":
        ...

    async def async_create_tree(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoGitTreesPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitTree]":
        url = f"/repos/{owner}/{repo}/git/trees"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoGitTreesPostBody).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=GitTree,
            error_models={
                "422": ValidationError,
                "404": BasicError,
                "403": BasicError,
            },
        )

    def get_tree(
        self,
        owner: str,
        repo: str,
        tree_sha: str,
        recursive: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[GitTree]":
        url = f"/repos/{owner}/{repo}/git/trees/{tree_sha}"

        params = {
            "recursive": recursive,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=GitTree,
            error_models={
                "422": ValidationError,
                "404": BasicError,
            },
        )

    async def async_get_tree(
        self,
        owner: str,
        repo: str,
        tree_sha: str,
        recursive: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[GitTree]":
        url = f"/repos/{owner}/{repo}/git/trees/{tree_sha}"

        params = {
            "recursive": recursive,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=GitTree,
            error_models={
                "422": ValidationError,
                "404": BasicError,
            },
        )
