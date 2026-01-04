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


class KandoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kando"

    @property
    def original_file_name(self) -> "str":
        return "kando.svg"

    @property
    def title(self) -> "str":
        return "Kando"

    @property
    def primary_color(self) -> "str":
        return "#EACFCF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kando</title>
     <path d="M22.953 6.435c-1.45 1.529-5.679 2.311-6.702
 1.291-1.022-1.019-.298-5.006 1.154-6.535a3.826 3.826 0 0 1 5.402-.146
 3.807 3.807 0 0 1 .146 5.39m-5.27
 12.74c-1.906-.904-3.96-4.674-3.303-5.96.656-1.287 4.68-1.83
 6.585-.926a3.824 3.813 0 0 1-3.282 6.886m-10.799.451c.274-2.088
 3.234-5.2 4.663-4.975s3.188 3.878 2.914 5.965a3.822 3.811 0 1
 1-7.578-.99M3.117 9.532c2.075-.388 5.959 1.454 6.187 2.878S6.6 16.638
 4.526 17.027a3.82 3.82 0 0 1-4.46-3.044 3.813 3.813 0 0 1
 3.051-4.45m8.466-6.707c1.01 1.849.453 6.103-.835 6.759S5.883 8.324
 4.873 6.474A3.824 3.813 0 0 1 6.4 1.302a3.82 3.81 0 0 1 5.183 1.524"
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
        return '''https://github.com/kando-menu/design/blob/650'''

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
