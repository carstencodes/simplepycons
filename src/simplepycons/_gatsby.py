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


class GatsbyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gatsby"

    @property
    def original_file_name(self) -> "str":
        return "gatsby.svg"

    @property
    def title(self) -> "str":
        return "Gatsby"

    @property
    def primary_color(self) -> "str":
        return "#663399"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gatsby</title>
     <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.6 0
 12 0zm0 2.571c3.171 0 5.915 1.543 7.629 3.858l-1.286 1.115C16.886
 5.572 14.571 4.286 12 4.286c-3.343 0-6.171 2.143-7.286 5.143l9.857
 9.857c2.486-.857 4.373-3 4.973-5.572h-4.115V12h6c0 4.457-3.172
 8.228-7.372 9.17L2.83 9.944C3.772 5.743 7.543 2.57 12 2.57zm-9.429
 9.6l9.344
 9.258c-2.4-.086-4.801-.943-6.601-2.743-1.8-1.8-2.743-4.201-2.743-6.515z"
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
