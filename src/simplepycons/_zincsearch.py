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


class ZincsearchIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zincsearch"

    @property
    def original_file_name(self) -> "str":
        return "zincsearch.svg"

    @property
    def title(self) -> "str":
        return "ZincSearch"

    @property
    def primary_color(self) -> "str":
        return "#5BA37F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ZincSearch</title>
     <path d="m18.723 19.748-1.73 1.493H.678L0 18.77l10.63-9.343.542
 6.635h8.701a3.649 3.649 0 0 1-1.15 3.686zM5.277
 4.252l1.73-1.493h16.316L24 5.23l-10.63 9.343-.542-6.635H4.129a3.648
 3.648 0 0 1 1.148-3.686Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/zincsearch/zincsearch-docs'''

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
