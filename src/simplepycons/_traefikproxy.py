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


class TraefikProxyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "traefikproxy"

    @property
    def original_file_name(self) -> "str":
        return "traefikproxy.svg"

    @property
    def title(self) -> "str":
        return "Traefik Proxy"

    @property
    def primary_color(self) -> "str":
        return "#24A1C1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Traefik Proxy</title>
     <path d="M12 1.19c1.088 0 2.056.768 2.056 1.714 0 .947-.921
 1.715-2.056 1.715-.13 0-.3-.022-.509-.064a.685.685 0 0
 0-.475.076l-7.37 4.195a.344.344 0 0 0 .001.597l7.99
 4.49c.208.116.461.116.669 0l8.034-4.468a.343.343 0 0 0
 .003-.598l-2.507-1.424a.683.683 0 0 0-.67-.003l-2.647 1.468a.234.234
 0 0 0-.119.18l-.001.025c0 .946-.921 1.714-2.056
 1.714s-2.056-.768-2.056-1.714c0-.947.921-1.715 2.056-1.715.042 0
 .09.002.145.007l.087.008.096.013a.685.685 0 0 0
 .425-.08l3.913-2.173c.3-.166.662-.171.965-.017l.04.023 5.465
 3.104c.686.39.693 1.368.03 1.773l-.037.021-3.656 2.033a.343.343 0 0 0
 .007.604l3.62 1.906c.72.378.736 1.402.03 1.804l-10.995 6.272a1.03
 1.03 0 0 1-1.019 0L.526 16.43a1.03 1.03 0 0 1
 .034-1.806l3.66-1.911a.343.343 0 0 0 .01-.603L.524 10.029a1.03 1.03 0
 0 1-.041-1.77l.036-.021L9.618 3.06a.688.688 0 0 0
 .308-.369l.011-.036c.32-.952 1.046-1.466 2.063-1.466Zm5.076
 12.63-4.492
 2.586-.041.022c-.306.158-.671.152-.973-.018l-4.478-2.527a.682.682 0 0
 0-.65-.01L3.86 15.224a.343.343 0 0 0-.012.602l7.887
 4.515c.21.12.467.121.677 0l7.956-4.547a.343.343 0 0
 0-.01-.602l-2.623-1.384a.683.683 0 0 0-.659.012z" />
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
