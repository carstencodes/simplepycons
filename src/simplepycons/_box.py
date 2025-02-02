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


class BoxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "box"

    @property
    def original_file_name(self) -> "str":
        return "box.svg"

    @property
    def title(self) -> "str":
        return "Box"

    @property
    def primary_color(self) -> "str":
        return "#0061D5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Box</title>
     <path d="M.959 5.523c-.54 0-.959.42-.959.899v7.549a4.59 4.59 0
 004.613 4.494 4.717 4.717 0 004.135-2.457c.779 1.438 2.337 2.457
 4.074 2.457 2.577 0 4.674-2.037
 4.674-4.613.06-2.457-2.037-4.495-4.613-4.495-1.738 0-3.295.959-4.074
 2.397-.78-1.438-2.338-2.397-4.135-2.397-1.079
 0-2.038.36-2.817.899V6.422a.92.92 0 00-.898-.899zM17.602 9.26a.95.95
 0 00-.704.158c-.36.3-.479.899-.18 1.318l2.397 3.116-2.396
 3.115c-.3.42-.24.96.18 1.26.419.3 1.016.298 1.316-.122l2.039-2.636
 2.096 2.697c.3.36.899.419
 1.318.12.36-.3.42-.84.121-1.259l-2.338-3.115
 2.338-3.057c.3-.419.298-1.018-.121-1.318-.48-.3-1.019-.24-1.318.18l-2.096
 2.576-2.04-2.695c-.149-.18-.373-.3-.612-.338zM4.613 11.154c1.558 0
 2.817 1.26 2.817 2.758 0 1.558-1.259 2.756-2.817 2.756-1.558
 0-2.816-1.198-2.816-2.756 0-1.498 1.258-2.758 2.816-2.758zm8.27
 0c1.558 0 2.816 1.26 2.816 2.758-.06 1.558-1.318 2.756-2.816
 2.756-1.558 0-2.817-1.198-2.817-2.756 0-1.498 1.259-2.758
 2.817-2.758Z" />
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
