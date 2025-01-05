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


class SensuIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sensu"

    @property
    def original_file_name(self) -> "str":
        return "sensu.svg"

    @property
    def title(self) -> "str":
        return "Sensu"

    @property
    def primary_color(self) -> "str":
        return "#89C967"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sensu</title>
     <path d="M24 12L12 0 0 12l12 12 12-12zM12 3.197l4.418
 4.418c-1.445-.386-2.93-.586-4.418-.586s-2.974.199-4.418.588L12
 3.196zM8.069 16.87c1.19-.658 2.534-1.008 3.931-1.008s2.741.35 3.931
 1.008L12 20.804 8.069
 16.87zm9.509-1.647c-1.697-1.08-3.636-1.622-5.578-1.622s-3.881.542-5.578
 1.622l-3.103-3.101C5.822 10.284 8.834 9.29 12 9.29s6.178.994 8.681
 2.832l-3.103 3.101z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/sensu/web/blob/c823738c11e'''

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
