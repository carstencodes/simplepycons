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


class DevboxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "devbox"

    @property
    def original_file_name(self) -> "str":
        return "devbox.svg"

    @property
    def title(self) -> "str":
        return "Devbox"

    @property
    def primary_color(self) -> "str":
        return "#280459"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Devbox</title>
     <path d="m19.546 7.5726-1.531-1.5703c-.4881.4371-.965.8647-1.442
 1.2922l-.959.8596c1.3076 1.3446 2.5887 2.6624 3.8756 3.987l-2.4261
 2.4956-1.4508 1.4924c.55.4988 1.0916.9897 1.6397 1.4864l.765.6933
 2.209-2.2773c1.2588-1.2976 2.5141-2.5916
 3.7736-3.8905v-.001a20797.5906 20797.5906 0 0 1-4.454-4.5674ZM2.992
 9.0716A16808.14 16808.14 0 0 1 0 12.141c2.0108 2.0727 3.9927 4.1152
 5.9838 6.1666l.5111-.4635c.638-.5786 1.2616-1.144
 1.8924-1.715l-1.447-1.4888c-.8134-.8368-1.6208-1.6676-2.431-2.5015
 1.0462-1.075 2.0745-2.132
 3.1094-3.1959l.7674-.7888c-.4342-.3892-.861-.7718-1.2883-1.1546l-1.114-.9983v.0011c-.9996
 1.0251-1.9958 2.0472-2.992 3.0694Zm12.585-6.0372c-1.317 6.199-2.6283
 12.3689-3.9453 18.5656l-.1962-.0387a2911.4317 2911.4317 0 0
 0-3.0284-.5957c.8529-4.0118 1.7034-8.0133 2.5549-12.0196L12.3533
 2.4z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/jetify-com/devbox/blob/c3c
ab01d7375726f0121a25fc0f5c838484246f7/docs/app/static/img/devbox_logo_'''

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
