#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class CleverCloudIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "clevercloud"

    @property
    def original_file_name(self) -> "str":
        return "clevercloud.svg"

    @property
    def title(self) -> "str":
        return "Clever Cloud"

    @property
    def primary_color(self) -> "str":
        return "#171C36"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Clever Cloud</title>
     <path d="M4 12.862.416 18.431 11.168 24ZM12.831 0 20
 11.139l3.584-5.57Zm-.001 24 10.753-5.569L20
 12.862Zm11.169-6.647V6.648L20.554 12ZM12 .43 4.832 11.568h14.336Zm0
 23.139 7.168-11.139H4.832Zm-8-12.43L11.168 0 .416 5.569ZM0
 6.647v10.707L3.445 12Z" />
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
