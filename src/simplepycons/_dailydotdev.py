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


class DailydotdevIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dailydotdev"

    @property
    def original_file_name(self) -> "str":
        return "dailydotdev.svg"

    @property
    def title(self) -> "str":
        return "daily.dev"

    @property
    def primary_color(self) -> "str":
        return "#CE3DF3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>daily.dev</title>
     <path d="M18.29 5.706a1.405 1.405 0 0 0-1.987 0L4.716
 17.296l1.324-2.65-2.65-2.649 3.312-3.311 2.65 2.65
 1.986-1.988-3.642-3.642a1.405 1.405 0 0 0-1.987 0L.411 11.004a1.404
 1.404 0 0 0 0 1.987l4.305 4.304.993.993a1.405 1.405 0 0 0 1.987
 0L19.285 6.7l-.993-.994Zm-.332 3.647 2.65 2.65-4.306 4.305a1.404
 1.404 0 1 0 1.986 1.986l5.299-5.298a1.404 1.404 0 0 0
 0-1.987l-4.305-4.304-1.324 2.648Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://brand.daily.dev/d/4gCtbahXkzKk/guidel'''

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
