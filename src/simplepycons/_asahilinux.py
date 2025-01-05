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


class AsahiLinuxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "asahilinux"

    @property
    def original_file_name(self) -> "str":
        return "asahilinux.svg"

    @property
    def title(self) -> "str":
        return "Asahi Linux"

    @property
    def primary_color(self) -> "str":
        return "#A61200"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Asahi Linux</title>
     <path d="m13.835 0-1.72 1.323v.97h2.178zm-1.95.057L9.81
 1.095l2.076 4.153zm.23 3.768V6.22l-1.057-2.113L6.43 5.678 12
 8.009l5.57-2.331zM6.21 5.835.533 15.957 11.885 24V8.21L6.222
 5.84Zm11.58 0-.012.004-5.6 2.345 7.512 10.449 3.777-2.675zm-3.955
 7.926v5.422l1.952-2.711zm2.864 3.981-4.411 6.135 5.846-4.14z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/AsahiLinux/artwork/blob/29
2637c9658c1491ddc1128fb6134aec01d904dd/logos/svg/AsahiLinux_logomark_m'''

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
