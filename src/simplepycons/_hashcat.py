#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class HashcatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hashcat"

    @property
    def original_file_name(self) -> "str":
        return "hashcat.svg"

    @property
    def title(self) -> "str":
        return "Hashcat"

    @property
    def primary_color(self) -> "str":
        return "#FFFFFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hashcat</title>
     <path d="M11.977 0c-.77.003-1.534.136-2.01.4C9.07.875 7.935.98
 6.51.663L5.453.453l.818.765c.977.924 1.664 2.428 1.664 3.67 0 1.029
 1.161 2.507 2.375 3.009.792.316.819.396.66 1.557-.791 5.887-1.504
 8.422-2.771 9.873-1.083 1.268-1.32 1.875-1.32
 3.326V24h10.295v-1.347c0-1.425-.237-2.032-1.267-3.273-1.293-1.557-2.217-4.752-2.64-9.16-.211-2.006-.185-2.086.396-2.218.924-.237
 2.402-2.059
 2.587-3.194.106-.554.238-1.346.317-1.742.053-.423.554-1.162
 1.056-1.663l.924-.925-1.03.185c-1.372.29-2.587.185-3.51-.29-.49-.25-1.261-.376-2.03-.373M9.039
 5.257h.004c.238 0 2.06 1.082 2.06 1.214 0
 .317-.872.026-1.505-.554-.39-.338-.652-.65-.56-.66m5.976.058c.097-.003-.097.195-.56.602-.396.37-.924.66-1.161.66-.528
 0-.37-.159.765-.792.557-.31.87-.468.956-.47" />
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
