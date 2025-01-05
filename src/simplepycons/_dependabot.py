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


class DependabotIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dependabot"

    @property
    def original_file_name(self) -> "str":
        return "dependabot.svg"

    @property
    def title(self) -> "str":
        return "Dependabot"

    @property
    def primary_color(self) -> "str":
        return "#025E8C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dependabot</title>
     <path d="M10.949.3136a1.918 1.918 0 012.102 0l9.3334
 6.1182c.541.354.866.957.866 1.604v7.9283c0 .647-.326 1.25-.866
 1.604l-9.3334 6.1183a1.918 1.918 0 01-2.102 0l-9.3334-6.1182a1.916
 1.916 0 01-.866-1.604V8.0358c0-.647.326-1.25.866-1.604zm1.801
 7.1862v.75H6.7498a.75.75 0 00-.75.7501V12h-.5a.25.25 0
 00-.25.25v2.5c0 .1381.112.2501.25.2501h.5v1.5c0
 .415.336.75.75.75h10.5004a.75.75 0 00.75-.75v-1.5h.5a.25.25 0
 00.25-.25v-2.5a.25.25 0 00-.25-.2501h-.5V8.9999a.75.75 0
 00-.75-.75H13.5V5.4998a.25.25 0 00-.25-.25H11.5a.25.25 0
 00-.25.25v1.75c0 .138.112.25.25.25zm3.2861 5.0892l-1.572
 1.572a.303.303 0 01-.428 0l-.947-.947a.303.303 0
 010-.428l.322-.322a.303.303 0 01.428 0l.41.411 1.037-1.036a.303.303 0
 01.428 0l.322.322a.303.303 0 010 .428zM9.464 14.16v.001a.303.303 0
 01-.428 0l-.948-.947a.302.302 0 010-.428l.323-.322a.303.303 0 01.427
 0l.412.411 1.036-1.037a.303.303 0 01.427 0l.323.322a.303.303 0 010
 .428z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
