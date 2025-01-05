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


class PalantirIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "palantir"

    @property
    def original_file_name(self) -> "str":
        return "palantir.svg"

    @property
    def title(self) -> "str":
        return "Palantir"

    @property
    def primary_color(self) -> "str":
        return "#101113"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Palantir</title>
     <path d="M20.147 18L12 21.178 3.853 18 2.5 20.343 12
 24l9.5-3.657L20.147 18zM12 0a9.5 9.5 0 1 0 0 19 9.5 9.5 0 0 0 0-19zm0
 16.078a6.568 6.568 0 1 1 0-13.136 6.568 6.568 0 0 1 0 13.136z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/palantir/conjure/blob/1b0d'''

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
