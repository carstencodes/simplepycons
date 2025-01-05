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


class DisqusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "disqus"

    @property
    def original_file_name(self) -> "str":
        return "disqus.svg"

    @property
    def title(self) -> "str":
        return "Disqus"

    @property
    def primary_color(self) -> "str":
        return "#2E9FFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Disqus</title>
     <path d="M12.438 23.654c-2.853 0-5.46-1.04-7.476-2.766L0
 21.568l1.917-4.733C1.25 15.36.875 13.725.875 12 .875 5.564 6.05.346
 12.44.346 18.82.346 24 5.564 24 12c0 6.438-5.176 11.654-11.562
 11.654zm6.315-11.687v-.033c0-3.363-2.373-5.76-6.462-5.76H7.877V17.83h4.35c4.12
 0 6.525-2.5 6.525-5.863h.004zm-6.415 2.998h-1.29V9.04h1.29c1.897 0
 3.157 1.08 3.157 2.945v.03c0 1.884-1.26 2.95-3.157 2.95z" />
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
