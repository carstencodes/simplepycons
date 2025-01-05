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


class ChevroletIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chevrolet"

    @property
    def original_file_name(self) -> "str":
        return "chevrolet.svg"

    @property
    def title(self) -> "str":
        return "Chevrolet"

    @property
    def primary_color(self) -> "str":
        return "#CD9834"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Chevrolet</title>
     <path d="M23.905 9.784H15.92V8.246a.157.157 0
 00-.157-.158H8.238a.157.157 0 00-.157.158v1.538H2.358c-.087
 0-.193.07-.237.158L.02 14.058c-.045.088-.011.157.077.157H8.08v1.54c0
 .086.07.157.157.157h7.525c.087 0 .157-.07.157-.157v-1.54h5.723c.087 0
 .193-.07.238-.157l2.1-4.116c.045-.087.011-.158-.076-.158m-2.494.996l-1.244
 2.437h-5.232v1.708H9.07v-1.708H2.595L3.84
 10.78h5.232V9.073h5.864v1.707z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.chevrolet.com/content/dam/chevrol
et/na/us/english/index/shopping-tools/download-catalog/02-pdf/2019-che'''

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
