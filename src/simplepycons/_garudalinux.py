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


class GarudaLinuxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "garudalinux"

    @property
    def original_file_name(self) -> "str":
        return "garudalinux.svg"

    @property
    def title(self) -> "str":
        return "Garuda Linux"

    @property
    def primary_color(self) -> "str":
        return "#8839EF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Garuda Linux</title>
     <path d="M10.24 3.179C6.82 6.579 3.366 10.064 0 13.465c2.4 2.406
 4.889 4.898 7.319 7.332l7.504.024 6.334-6.316-13.754-.012-1.525 1.54
 11.512.024-3.198 3.197H7.956L2.172 13.47l8.74-8.74h6.284l4.815
 4.815-7.501-.01v-2.12l-3.68 3.68c3.873.004 7.746.003 11.62
 0v2.102l1.55-1.55-.003-2.306-6.16-6.159z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://gitlab.com/garuda-linux/themes-and-se
ttings/artwork/garuda-icons/-/blob/aab26625fe01479ebc3a252103fca723bac'''

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
