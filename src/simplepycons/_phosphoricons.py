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


class PhosphorIconsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "phosphoricons"

    @property
    def original_file_name(self) -> "str":
        return "phosphoricons.svg"

    @property
    def title(self) -> "str":
        return "Phosphor Icons"

    @property
    def primary_color(self) -> "str":
        return "#3C402B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Phosphor Icons</title>
     <path d="M12.404.001H3.866a.618.618 0 0 0-.619.619v15.173A8.217
 8.217 0 0 0 11.449 24a.617.617 0 0 0 .618-.619v-6.969h.332a8.204
 8.204 0 0 0 7.715-5.031 8.216 8.216 0 0 0 0-6.349A8.214 8.214 0 0 0
 12.399.001h.005Zm-1.579 22.736a6.98 6.98 0 0
 1-6.317-6.317h6.317v6.317Zm0-9.562L4.869 1.238h5.967l-.011
 11.937Zm1.579 2h-.331V1.238h.331a6.975 6.975 0 0 1 5.016 1.993 6.986
 6.986 0 0 1 1.546 2.277 6.987 6.987 0 0 1 0 5.397 6.975 6.975 0 0
 1-6.562 4.27Z" />
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
