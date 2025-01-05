#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class CampaignMonitorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "campaignmonitor"

    @property
    def original_file_name(self) -> "str":
        return "campaignmonitor.svg"

    @property
    def title(self) -> "str":
        return "Campaign Monitor"

    @property
    def primary_color(self) -> "str":
        return "#111324"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Campaign Monitor</title>
     <path d="M23.836 4.27c-.29-.413-.86-.515-1.273-.226L.163
 19.73c.167.235.437.39.747.39h22.18c.503 0
 .91-.41.91-.914V4.78c-.004-.176-.058-.352-.164-.51zm-22.4-.226c-.413-.29-.982-.19-1.272.226-.107.154-.162.332-.164.51v14.45l10.664-8.736-9.227-6.45v-.002z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.campaignmonitor.com/company/brand'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
