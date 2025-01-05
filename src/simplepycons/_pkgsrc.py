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


class PkgsrcIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pkgsrc"

    @property
    def original_file_name(self) -> "str":
        return "pkgsrc.svg"

    @property
    def title(self) -> "str":
        return "pkgsrc"

    @property
    def primary_color(self) -> "str":
        return "#FF6600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>pkgsrc</title>
     <path d="m12.908 8.763 9.157-5.132L11.25 0 1.62 4.42Zm1.5 2.29
 9-5.368-.948 11.84-8.191 6.382zM.593 6.712 1.619 18.79 11.922
 24l-.12-12.788Z" />
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
