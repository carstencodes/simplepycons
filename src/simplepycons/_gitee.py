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


class GiteeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gitee"

    @property
    def original_file_name(self) -> "str":
        return "gitee.svg"

    @property
    def title(self) -> "str":
        return "Gitee"

    @property
    def primary_color(self) -> "str":
        return "#C71D23"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gitee</title>
     <path d="M11.984 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.016 0zm6.09 5.333c.328 0
 .593.266.592.593v1.482a.594.594 0 0 1-.593.592H9.777c-.982
 0-1.778.796-1.778 1.778v5.63c0 .327.266.592.593.592h5.63c.982 0
 1.778-.796 1.778-1.778v-.296a.593.593 0 0 0-.592-.593h-4.15a.592.592
 0 0 1-.592-.592v-1.482a.593.593 0 0 1 .593-.592h6.815c.327 0
 .593.265.593.592v3.408a4 4 0 0 1-4 4H5.926a.593.593 0 0
 1-.593-.593V9.778a4.444 4.444 0 0 1 4.445-4.444h8.296Z" />
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
