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


class WebcomponentsdotorgIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "webcomponentsdotorg"

    @property
    def original_file_name(self) -> "str":
        return "webcomponentsdotorg.svg"

    @property
    def title(self) -> "str":
        return "webcomponents.org"

    @property
    def primary_color(self) -> "str":
        return "#29ABE2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>webcomponents.org</title>
     <path d="M11.731 2.225l-.01.016H5.618L0 11.979l5.618
 9.736h12.8l.04.06
 2.134-3.735.518-.893h-.008l.008-.014-.626-.75h.895l.006-.01.008.01L24
 11.994l-2.607-4.39-.003.005-.011-.02h-.945l.63-.763-2.606-4.57-.006.01-.024-.04H11.73zM9.107
 6.824h6.19l-.53.764h-.023l2.398
 4.015h.875l-.277.328.357.435h-.956l-2.398
 4.015h.027l.523.764H9.074l-2.99-5.168 3.022-5.155z" />
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
