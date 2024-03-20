"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class EnterprisesEnterpriseCodeSecurityAndAnalysisPatchBody(GitHubModel):
    """EnterprisesEnterpriseCodeSecurityAndAnalysisPatchBody"""

    advanced_security_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description='Whether GitHub Advanced Security is automatically enabled for new repositories. For more information, see "[About GitHub Advanced Security](https://docs.github.com/enterprise-cloud@latest//get-started/learning-about-github/about-github-advanced-security)."',
    )
    advanced_security_enabled_new_user_namespace_repos: Missing[bool] = Field(
        default=UNSET,
        description='Whether GitHub Advanced Security is automatically enabled for new user namespace repositories. For more information, see "[About GitHub Advanced Security](https://docs.github.com/enterprise-cloud@latest//get-started/learning-about-github/about-github-advanced-security)."',
    )
    dependabot_alerts_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description='Whether Dependabot alerts are automatically enabled for new repositories. For more information, see "[About Dependabot alerts](https://docs.github.com/enterprise-cloud@latest//code-security/dependabot/dependabot-alerts/about-dependabot-alerts)."',
    )
    secret_scanning_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description='Whether secret scanning is automatically enabled for new repositories. For more information, see "[About secret scanning](https://docs.github.com/enterprise-cloud@latest//code-security/secret-scanning/about-secret-scanning)."',
    )
    secret_scanning_push_protection_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description='Whether secret scanning push protection is automatically enabled for new repositories. For more information, see "[Protecting pushes with secret scanning](https://docs.github.com/enterprise-cloud@latest//code-security/secret-scanning/protecting-pushes-with-secret-scanning)."',
    )
    secret_scanning_push_protection_custom_link: Missing[Union[str, None]] = Field(
        default=UNSET,
        description='The URL that will be displayed to contributors who are blocked from pushing a secret. For more information, see "[Protecting pushes with secret scanning](https://docs.github.com/enterprise-cloud@latest//code-security/secret-scanning/protecting-pushes-with-secret-scanning)."\nTo disable this functionality, set this field to `null`.',
    )
    secret_scanning_validity_checks_enabled: Missing[Union[bool, None]] = Field(
        default=UNSET,
        description="Whether secret scanning automatic validity checks on supported partner tokens is enabled for all repositories under this enterprise.",
    )


model_rebuild(EnterprisesEnterpriseCodeSecurityAndAnalysisPatchBody)

__all__ = ("EnterprisesEnterpriseCodeSecurityAndAnalysisPatchBody",)
